function tiempo_verde = control_semaforos(tiempo_actual)
    ciclo_semaforo = 60; % total del ciclo del semáforo en segundos
    verde_inicial = 20; % inicial del semáforo en verde
    
    tiempo_verde = mod(tiempo_actual, ciclo_semaforo);
    if tiempo_verde < verde_inicial
        tiempo_verde = verde_inicial;
    end
    
    % Graficar el resultado
    t = 0:0.1:ciclo_semaforo;
    v = mod(t, ciclo_semaforo);
    v(v < verde_inicial) = verde_inicial;
    
    figure;
    plot(t, v, 'LineWidth', 2);
    xlabel('Tiempo (s)');
    ylabel('Tiempo Verde del Semáforo (s)');
    title('Duración del Tiempo Verde del Semáforo en un Ciclo');
    
    % Imprimir el resultado en consola
    disp(['El tiempo verde del semáforo en el segundo ' num2str(tiempo_actual) ' es: ' num2str(tiempo_verde) ' segundos']);
end

% Llamada a la funcion
tiempo_actual = 65;
tiempo_verde = control_semaforos(tiempo_actual);
