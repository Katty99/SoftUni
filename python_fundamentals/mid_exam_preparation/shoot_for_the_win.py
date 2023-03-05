targets = [int(x) for x in input().split()]
shot_targets = 0
while True:
    command = input()
    if command == 'End':
        break
    else:
        command = int(command)
        if 0 <= command < len(targets):
            shot = targets[command]
            targets[command] = -1
            shot_targets += 1
            for index in range(len(targets)):
                if targets[index] == -1:
                    continue
                if targets[index] > shot:
                    targets[index] -= shot
                else:
                    targets[index] += shot
final_list = []
for current in range(len(targets)):
    final_list.append(str(targets[current]))
print(f"Shot targets: {shot_targets} -> {' '.join(final_list)}")