import re
import csv


def processLog(logSolver, outputData):
    print(f'Tentando gravar os dados em {outputData}...')

    def extract_residual(line):
        match = re.search(r'Final residual = ([\d.e+-]+)', line)
        if match:
            return match.group(1)
        return None

    with open(logSolver, 'r') as infile, open(outputData, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['time', 'Ux', 'Uy', 'epsilon', 'k', 'p'])
        
        current_time = None
        ux_residual = None
        uy_residual = None
        epsilon_residual = None
        k_residual = None
        p_residual = None
        
        for line in infile:
            time_match = re.search(r'Time = ([\d.]+)', line)
            if time_match:
                if current_time is not None and ux_residual is not None:
                    csv_writer.writerow([current_time, ux_residual, uy_residual, epsilon_residual, k_residual, p_residual])
                
                current_time = time_match.group(1)
                ux_residual = None
                uy_residual = None
                epsilon_residual = None
                k_residual = None
                p_residual = None
            
            if 'Solving for Ux' in line:
                ux_residual = extract_residual(line)
            
            if 'Solving for Uy' in line:
                uy_residual = extract_residual(line)
                
            if 'Solving for epsilon' in line:
                epsilon_residual = extract_residual(line)
                
            if 'Solving for k' in line:
                k_residual = extract_residual(line)
                
            if 'Solving for p' in line:
                p_residual = extract_residual(line)
        
        if current_time is not None and ux_residual is not None:
            csv_writer.writerow([current_time, ux_residual, uy_residual, epsilon_residual, k_residual, p_residual])

    print(f'Os resultados foram gravados em {outputData} com sucesso!')
    
if __name__ == "__main__":
    processLog()