import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import warnings

# 过滤sklearn的数值计算警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='sklearn')
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

df_cirrhosis = pd.read_csv("cleaned_cirrhosis.csv")

# 特征工程和编码
# 将目标变量Status映射为数值：D, C, CL
status_mapping = {
    'D': 1,  # Deceased
    'C': 0,  # Censor
    'CL': 0  # Censor (transplant)
}
df_cirrhosis["Status_Encoded"] = df_cirrhosis["Status"].map(status_mapping)

# 对分类变量进行One-Hot编码
df_cirrhosis = pd.get_dummies(df_cirrhosis, columns=[
    'Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Stage'
], drop_first=True)

# 删除原始Status列和ID列
df_cirrhosis = df_cirrhosis.drop(["Status"], axis=1)

# 分离特征和目标变量
X = df_cirrhosis.drop("Status_Encoded", axis=1)
y = df_cirrhosis["Status_Encoded"]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 特征缩放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 构建逻辑回归模型
model = LogisticRegression(random_state=42, solver='liblinear')
model.fit(X_train_scaled, y_train)

# 模型预测
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

# 模型评估
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
class_report = classification_report(y_test, y_pred)

print(f"\n--- Cirrhosis Prediction Model Evaluation ---")
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
plt.title('Receiver Operating Characteristic (ROC) Curve for Cirrhosis Prediction')
plt.legend(loc='lower right')
plt.savefig("cirrhosis_roc_curve.png")
plt.close()

# 特征重要性分析
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("\nFeature Importance (Logistic Regression Coefficients):\n", feature_importance)

print("Cirrhosis prediction model built and evaluated. Results saved.")
