import matplotlib.pyplot as plt

data_dir = "./data/" 
acc_norm = data_dir + "acc_norm.txt"

of = open(acc_norm)
of.readline()  # ignore the first line

acc_norm_raw_list = []
acc_norm_correct_list = []

for line in of:
    data = line.split(',')
    assert len(data) == 2
    acc_norm_raw = float(data[0])
    acc_norm_cor = float(data[1])
    if acc_norm_raw > 9.5 and acc_norm_raw < 10.5:
        acc_norm_raw_list.append(acc_norm_raw)
        acc_norm_correct_list.append(acc_norm_cor)

G = 9.8016

idx = range(len(acc_norm_raw_list))
plt.plot(idx, acc_norm_raw_list, '-b', idx, acc_norm_correct_list, '-r')
plt.axhline(y=G, color='g', linestyle='-')
plt.title("Norm of Acc (G = %.4f)" % G)
plt.ylabel("norm (m/s/s)")
plt.legend(labels=['raw acc', 'corrected acc'])
plt.show()
      
of.close()