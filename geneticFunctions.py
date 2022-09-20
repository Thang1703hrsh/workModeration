## Source tính toán một số giá trị trong thuật toán di truyền và sắp xếp tối ưu 

import os
import random
import time
from functools import reduce
import numpy as np

#Tính makespan cho mỗi thuật toán
def calc_makespan(solution, proccessing_time, number_of_jobs, number_of_machines):
    # Danh sách thời gian trôi qua cho tới khi hoàn thành công việc 
    cost = [0] * number_of_jobs
    # Đối với mỗi máy, tổng thời gian đã được thông qua sẽ được cập nhật 
    for machine_no in range(0, number_of_machines):
        for slot in range(number_of_jobs):
            # Thời gian trôi qua cho tới khi công việc bắt đầu xử lý
            cost_so_far = cost[slot]
            if slot > 0:
                cost_so_far = max(cost[slot - 1], cost[slot])
            cost[slot] = cost_so_far + proccessing_time[solution[slot]][machine_no]
    return cost[number_of_jobs - 1]

def initialize_population(population_size, number_of_jobs):
    population = []
    i = 0
    while i < population_size:
        individual = list(np.random.permutation(number_of_jobs))
        if individual not in population:
            population.append(individual)
            i += 1

    return population

# Hai điểm chéo nhau là tập hợp các công việc giữa hai 
# Hai điểm được chọn ngẫu nhiên # luôn được thừa kế từ cha sang con, 
# Các công việc khác được đặt trong cùng một cách như chéo một điểm.
 
def crossover(parents):
    parent1 = parents[0]
    parent2 = parents[1]
    length_of_parent = len(parent1)
    first_point = int(length_of_parent / 2 - length_of_parent / 4)
    second_point = int(length_of_parent - first_point)
    intersect = parent1[first_point:second_point]

    child = []
    index = 0
    for pos2 in range(len(parent2)):
        if first_point <= index < second_point:
            child.extend(intersect)
            index = second_point
        if parent2[pos2] not in intersect:
                child.append(parent2[pos2])
                index += 1

    return child

# Hàm Áp dụng đột biến cho một giải pháp hiện có bằng cách sử dụng toán tử di chuyển swap 
def mutation(solution):
    # Sao chép giải pháp
    mutated_solution = list(solution)
    solution_length = len(solution)
    # Chọn hai vị trí để chuyển đổi ngẫu nhiên
    swap_positions = list(np.random.permutation(np.arange(solution_length))[:2])
    first_job = solution[swap_positions[0]]
    second_job = solution[swap_positions[1]]
    mutated_solution[swap_positions[0]] = second_job
    mutated_solution[swap_positions[1]] = first_job
    return mutated_solution

# Selects parent by binary tournament method
# Chọn cha mẹ bằng phương pháp giải đấu nhị phân
def select_parent(population, processing_time, number_of_jobs, number_of_machines):
    parent_pairs = []
    # randomly choose how many parent pairs will be selected
    # Chọn ngẫu nhiên số cặp cha sẽ được chọn
    parent_pair_count = random.randint(2, int(len(population)/2))
    for k in range(parent_pair_count):
        parent1 = binary_tournament(number_of_jobs, number_of_machines, population, processing_time)
        parent2 = binary_tournament(number_of_jobs, number_of_machines, population, processing_time)
        if parent1 != parent2 and (parent1, parent2) not in parent_pairs:
            parent_pairs.append((parent1, parent2))
    return parent_pairs

def binary_tournament(number_of_jobs, number_of_machines, population, processing_time):
    parent = []
    candidates = random.sample(population, 2)
    makespan1 = calc_makespan(candidates[0], processing_time, number_of_jobs, number_of_machines)
    makespan2 = calc_makespan(candidates[1], processing_time, number_of_jobs, number_of_machines)
    if makespan1 < makespan2:
        parent = candidates[0]
    else:
        parent = candidates[1]
    return parent

def update_population(population, children,processing_time,no_of_jobs,no_of_machines):
    costed_population = []
    for individual in population:
        ind_makespan = (calc_makespan(individual, processing_time, no_of_jobs, no_of_machines), individual)
        costed_population.append(ind_makespan)
    costed_population.sort(key=lambda x: x[0], reverse=True)

    costed_children = []
    for individual in children:
        ind_makespan = (calc_makespan(individual, processing_time, no_of_jobs, no_of_machines), individual)
        costed_children.append(ind_makespan)
    costed_children.sort(key=lambda x: x[0])
    for child in costed_children:
        if child not in population:
            population.append(individual)
            population.remove(costed_population[0][1])
            break