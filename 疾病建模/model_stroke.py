# 修复目标变量编码问题
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, precision_recall_curve
import matplotlib.pyplot as plt
import numpy as np
import warnings

# 过滤sklearn的数值计算警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='sklearn')
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

# 读取已清理的数据
df_stroke = pd.read_csv("cleaned_stroke.csv")

# 特征工程和编码
df_stroke = pd.get_dummies(df_stroke,
                           columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status',
                                    'hypertension', 'heart_disease'], drop_first=True)

# 编码目标变量
le = LabelEncoder()
df_stroke['stroke_encoded'] = le.fit_transform(df_stroke['stroke'])
print(f"目标变量映射: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# 分离特征和目标变量
X = df_stroke.drop(['stroke', 'stroke_encoded'], axis=1)
y = df_stroke['stroke_encoded']

# 添加：数据不平衡分析
print("\n=== 数据不平衡分析 ===")
print(f"特征数量: {X.shape[1]}")
print(f"目标变量分布:\n{y.value_counts()}")
print(f"正例比例: {y.mean():.4f}")

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 特征缩放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 使用平衡权重的逻辑回归模型
model = LogisticRegression(
    random_state=42,
    solver='liblinear',
    class_weight='balanced',
    max_iter=1000
)
model.fit(X_train_scaled, y_train)

# 模型预测
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

# 找到最佳分类阈值
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)
f1_scores = 2 * (precision * recall) / (precision + recall)
best_threshold_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_threshold_idx]

print(f"\n=== 阈值优化 ===")
print(f"默认阈值(0.5)预测正例数: {(y_pred == 1).sum()}")
print(f"最佳阈值: {best_threshold:.4f}")

# 使用最佳阈值重新预测
y_pred_optimal = (y_pred_proba >= best_threshold).astype(int)
print(f"最佳阈值预测正例数: {(y_pred_optimal == 1).sum()}")

# 模型评估
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

# 默认阈值评估
class_report = classification_report(
    y_test, y_pred,
    zero_division=0,
    target_names=['No Stroke', 'Stroke']
)

# 最佳阈值评估
accuracy_optimal = accuracy_score(y_test, y_pred_optimal)
class_report_optimal = classification_report(
    y_test, y_pred_optimal,
    zero_division=0,
    target_names=['No Stroke', 'Stroke']
)

print(f"\n--- Stroke Prediction Model Evaluation ---")
print(f"Accuracy (默认阈值): {accuracy:.4f}")
print(f"Accuracy (最佳阈值): {accuracy_optimal:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")
print("\nClassification Report (默认阈值):\n", class_report)
print(f"\nClassification Report (最佳阈值 {best_threshold:.3f}):\n", class_report_optimal)

# 绘制综合分析图
plt.figure(figsize=(15, 5))

# ROC曲线
plt.subplot(1, 3, 1)
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)

# Precision-Recall曲线
plt.subplot(1, 3, 2)
plt.plot(recall, precision, color='blue', lw=2, label='PR curve')
plt.axvline(x=recall[best_threshold_idx], color='red', linestyle='--',
            label=f'Best threshold: {best_threshold:.3f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.grid(True, alpha=0.3)

# 预测概率分布
plt.subplot(1, 3, 3)
plt.hist(y_pred_proba[y_test == 0], bins=50, alpha=0.7, label='No Stroke', color='blue')
plt.hist(y_pred_proba[y_test == 1], bins=50, alpha=0.7, label='Stroke', color='red')
plt.axvline(x=0.5, color='black', linestyle='--', label='Default threshold')
plt.axvline(x=best_threshold, color='green', linestyle='--', label='Optimal threshold')
plt.xlabel('Predicted Probability')
plt.ylabel('Frequency')
plt.title('Prediction Probability Distribution')
plt.legend()

plt.tight_layout()
plt.savefig("stroke_comprehensive_analysis.png", dpi=300, bbox_inches='tight')
plt.show()

# 特征重要性分析
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', key=abs, ascending=False)

print("\nFeature Importance (Logistic Regression Coefficients):\n", feature_importance.head(10))

print("Stroke prediction model built and evaluated. Results saved.")
