
from data_preprocess import X_train, X_test, y_train, y_test, loan_intent_encoder


from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def evaluate_model(y_pred, y_test):
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print(f"Accuracy: {round(acc, 3)}")
    print(f"F1 Score: {round(f1, 3)}")
    print(f"Precision: {round(precision, 3)}")
    print(f"Recall: {round(recall, 3)}")


# Random Forest
from sklearn.ensemble import RandomForestClassifier

n_estimators = 150
max_depth = 9
max_features = 6
random_state = 42

# Instantiate model
rf_model = RandomForestClassifier(n_estimators = n_estimators,
                                  max_depth = max_depth,
                                  max_features = max_features,
                                  random_state = random_state)

# Train model
rf_model.fit(X_train, y_train)

print("Model trained successfully!")


# Show model performance on testing set
y_pred = rf_model.predict(X_test)

evaluate_model(y_test, y_pred)


# Save model
import joblib
joblib.dump(rf_model, "trained_model/rf_model_loan_default_pred.pkl")


# save encoder
joblib.dump(loan_intent_encoder, "trained_model/loan_intent_encoder.pkl")

