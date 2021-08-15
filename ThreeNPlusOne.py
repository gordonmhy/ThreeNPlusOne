import random

from matplotlib import pyplot as plt


def gen_func(x, y, prev_num=None):
    if prev_num != 1:
        if len(x) == 0:
            x += [1]
            num = random.randint(2, 100)
            y += [num]
        else:
            x += [len(x) + 1]
            num = 3 * prev_num + 1 if prev_num % 2 != 0 else prev_num // 2
            y += [num]
        gen_func(x, y, num)


for i in range(10):
    x, y = [], []
    gen_func(x, y)
    plt.plot(x, y, label=str(y[0]), marker='.')

plt.title('Three N Plus One')
plt.xlabel('Iteration')
plt.ylabel('N')
plt.legend()
# plt.savefig('PlotEx.png', format='png')
plt.show()
