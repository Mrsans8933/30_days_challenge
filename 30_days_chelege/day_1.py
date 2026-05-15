import time

bar = ["█"]
for i in range(1, 101):
    print(f"\r {i}% {''.join(bar)}", end="")
    bar.append("█")
    time.sleep(0.3)
print("Визуальная загрузка завершенна")