function velocidad = greenshields(densidad)
    vmax = 120;
    rho_max = 100;
    rho_c = 30;
    
    if densidad <= rho_c
        velocidad = vmax * (1 - densidad / rho_max);
    else
        velocidad = 0; % Congestion total
    end
    
    % Graficar el resultado
    densidad = 0:1:100; % Valores de densidad para graficar
    velocidad = vmax * (1 - densidad / rho_max); % Calculamos la velocidad para cada densidad
    velocidad(densidad > rho_c) = 0; % Congestion total
    figure;
    plot(densidad, velocidad, 'LineWidth', 2);
    xlabel('Densidad de vehículos');
    ylabel('Velocidad de flujo de tráfico (km/h)');
    title('Modelo de Flujo de Tráfico de Greenshields');
    
    % Imprimir el resultado en consola
    disp(['La velocidad de flujo de tráfico para una densidad de ' num2str(densidad) ' vehículos es: ' num2str(velocidad) ' km/h']);
end

% Llamada a la funcion greenshields
densidad = 50;
velocidad = greenshields(densidad);
