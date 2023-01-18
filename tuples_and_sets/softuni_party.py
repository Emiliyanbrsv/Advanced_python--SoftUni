iterations = int(input())
guests = set(input() for name in range(iterations))
arrived_guest = set()
COMMAND_END = "END"

while True:
    command = input()
    if command == COMMAND_END:
        break
    arrived_guest.add(command)

not_arrived = guests.difference(arrived_guest)
print(len(not_arrived))
for guest in sorted(not_arrived):
    print(guest)
