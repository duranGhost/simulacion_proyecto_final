function densidad_nueva = lwr(densidad, velocidad_flujo)
    % Asegurar que ambas matrices tengan la misma longitud
    min_length = min(length(densidad), length(velocidad_flujo));
    densidad = densidad(1:min_length);
    velocidad_flujo = velocidad_flujo(1:min_length);
    
    longitud_tramo = 1; % Longitud del tramo de carretera
    dt = 0.1; % Paso de tiempo
    dx = 0.1; % Paso espacial
    
    % Calculo nueva densidad
    densidad_nueva = densidad - (dt / dx) * (velocidad_flujo(2:end) - velocidad_flujo(1:end-1)) / longitud_tramo;
    
    disp('La densidad de vehículos después de la operación es:');
    disp(densidad_nueva);
    
    t = dt:dt:length(densidad_nueva)*dt;
    figure;
    plot(t, densidad_nueva, 'LineWidth', 2);
    xlabel('Tiempo (s)');
    ylabel('Densidad de vehículos');
    title('Evolución de la Densidad de Vehículos en un Tramo de Carretera (Modelo LWR)');
end

densidad_inicial = [20 30 40 50 60];
velocidad_flujo = [80 70];
densidad_nueva = lwr(densidad_inicial, velocidad_flujo);
