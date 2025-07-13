import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np
import warnings

# 过滤sklearn的数值计算警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='sklearn')
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

# 读取已清理的数据
df_heart = pd.read_csv("cleaned_heart.csv")

# 对分类变量进行One-Hot编码
df_heart = pd.get_dummies(df_heart, columns=[
    'Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope', 'FastingBS'
], drop_first=True)

# 将目标变量转换为数值格式
le = LabelEncoder()
df_heart['HeartDisease'] = le.fit_transform(df_heart['HeartDisease'])
print(f"目标变量映射: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# 分离特征和目标变量
X = df_heart.drop('HeartDisease', axis=1)
y = df_heart['HeartDisease']

# 确保数据类型正确
X = X.astype('float64')

# 数值稳定性检查
X = X.replace([np.inf, -np.inf], np.nan)
if X.isnull().any().any():
    X = X.fillna(X.median())

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 使用RobustScaler进行特征缩放
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 构建逻辑回归模型
model = LogisticRegression(
    random_state=42,
    solver='lbfgs',  # 更稳定的求解器
    C=10.0,  # 降低正则化强度
    max_iter=2000  # 增加最大迭代次数
)

# 训练模型
model.fit(X_train_scaled, y_train)

# 模型预测
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

# 模型评估
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
class_report = classification_report(y_test, y_pred)

print(f"\n--- Heart Disease Prediction Model Evaluation ---")
print(f"Accuracy: {accuracy:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")
print("Classification Report:\n", class_report)

# 绘制ROC曲线
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for Heart Disease Prediction')
plt.legend(loc='lower right')
plt.savefig("heart_roc_curve.png", dpi=300, bbox_inches='tight')
plt.close()

# 特征重要性分析
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("\nFeature Importance (Logistic Regression Coefficients):\n", feature_importance)
print("Heart disease prediction model built and evaluated. Results saved.")
