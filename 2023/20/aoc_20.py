# Advent of code Day 20

## Part one
# Import libraries
from collections import deque, Counter
from dataclasses import dataclass
import math

# Read and preprocess the file
with open("input.txt", "r") as file:
    lines = [line.strip().replace(",", "").split() for line in file]


# Define flip flop module
@dataclass
class FlipFlop:
    def __init__(self, line):
        self.status = 0  # Default to off
        self.source = line[0]
        self.destinations = line[2:]

    def receive_pulse(self, pulse):
        self.input = pulse[1]
        if self.input == 1:
            pass
        else:
            self.status = abs(self.status - 1)

    def build_pulse(self):
        if self.input == 0:
            self.pulse_build = [
                (self.source, self.status, destination)
                for destination in self.destinations
            ]
        else:
            self.pulse_build = None

        return self.pulse_build


# Define conjunction module
@dataclass
class Conjunction:
    def __init__(self, line, targets):
        self.source = line[0]
        self.destinations = line[2:]
        self.inputs = targets[1:]
        self.status = {target: 0 for target in targets}

    def receive_pulse(self, pulse):
        self.status[pulse[0]] = pulse[1]

        if sum(self.status.values()) == len(self.status.values()):
            self.pulse_send = 0
        else:
            self.pulse_send = 1

    def build_pulse(self):
        self.pulse_build = [
            (self.source, self.pulse_send, destination)
            for destination in self.destinations
        ]
        return self.pulse_build


# Define the computer
class Board:
    def __init__(self, board, part_two_input=None):

        # P2 specific
        self.part_two_input = part_two_input

        # Easily define flip-flop and broadcast inputs
        self.broadcaster = [line for line in board if "broadcaster" in line][0]
        self.flip_flop = [[line[0][1:]] + line[1:] for line in board if "%" in line[0]]

        # Conjunction modules need target modules
        self.conjunction = []
        for line in [line for line in board if "&" in line[0]]:

            self.temporary_line = [line[0][1:]] + line[1:]
            temp_item = []

            for x in lines:
                if self.temporary_line[0] in x[1:]:
                    temp_item.append(x[0][1:])

            self.conjunction.append([self.temporary_line, temp_item])

        # Define dictionary containing modules
        ## Add flip-flops
        self.dict = {
            self.flip_flop[i][0]: FlipFlop(self.flip_flop[i])
            for i in range(len(self.flip_flop))
        }

        ## Add conjunctions
        for i in range(len(self.conjunction)):
            self.dict[self.conjunction[i][0][0]] = Conjunction(
                self.conjunction[i][0], self.conjunction[i][1]
            )

        ## Define initial pulse
        self.broadcast_pulse = [
            (self.broadcaster[0], 0, destination)
            for destination in self.broadcaster[2:]
        ]

    def send_pulse(self):
        self.signal = self.queue.popleft()

        # Send counter info
        self.pulse_counts[self.signal[1]] += 1

        ## Part 2
        if self.p2 and self.signal[2] in self.part_two_input[0] and self.signal[1] == 1:
            self.part_two_solution.append(self.part_two_counter)
            pass

        # Ignore writing to non existent modules
        if self.signal[2] not in self.dict.keys():
            pass
        else:

            self.module = self.dict[self.signal[2]]

            self.module.receive_pulse(self.signal)
            self.pulses = self.module.build_pulse()

            if self.pulses:
                for pulse in self.pulses:
                    self.queue.append(pulse)

    def press_button(self, p2=False):

        self.p2 = p2

        self.queue = deque(self.broadcast_pulse)
        self.pulse_counts = Counter({0: 1})

        while self.queue:

            self.send_pulse()

        return self.pulse_counts

    def count_pulses(self):
        total = sum((self.press_button() for _ in range(1000)), Counter())

        return total[0] * total[1]

    def part_two(self):

        self.part_two_counter = 0
        self.part_two_solution = []

        for _ in range(5000):
            self.part_two_counter += 1

            self.press_button(p2=True)

            if len(self.part_two_solution) >= 4:
                self.answer = self.part_two_solution[0]
                for num in self.part_two_solution:
                    self.answer = abs(self.answer * num) // math.gcd(self.answer, num)
                print(self.answer)
                break


# Finish part one
Board(lines).count_pulses()
## Part two
for x in lines:
    if "rx" in x:
        rx_signal_sender = x[0][1:]

signal_senders = []
for x in lines:
    if rx_signal_sender in x:
        signal_senders.append(x[0][1:])

part_two_input = [rx_signal_sender] + signal_senders
print(part_two_input)
Board(lines, part_two_input).part_two()
