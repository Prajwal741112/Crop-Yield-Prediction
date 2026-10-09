qsvm_accuracy = 99.09
qlr_accuracy = 95.68
qrf_accuracy = 99.09

print("========== MODEL COMPARISON ==========")

print(f"Q-SVM Accuracy : {qsvm_accuracy}%")
print(f"Q-LR Accuracy  : {qlr_accuracy}%")
print(f"QRF Accuracy   : {qrf_accuracy}%")

print("\nBest Model:")

if qsvm_accuracy >= qlr_accuracy and qsvm_accuracy >= qrf_accuracy:
    print("Q-SVM")
elif qlr_accuracy >= qsvm_accuracy and qlr_accuracy >= qrf_accuracy:
    print("Q-LR")
else:
    print("QRF")