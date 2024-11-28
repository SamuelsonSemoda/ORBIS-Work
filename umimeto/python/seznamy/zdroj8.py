#Napište funkci max_pair_sum(num_list), která pro zadaný seznam kladných čísel num_list vypočítá nejvyšší součet dvou po sobě jdoucích čísel.

def max_pair_sum(num_list):
  if len(num_list) < 2:
    return None
    
  max_sum = max(num_list[i] + num_list[i+1] for i in range(len(num_list) - 1))
    return max_sum
