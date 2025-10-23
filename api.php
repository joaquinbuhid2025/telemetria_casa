<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');

$dataFile = 'data.json';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recibir datos del sistema Python
    $input = file_get_contents('php://input');
    $data = json_decode($input, true);
    
    if ($data) {
        // Guardar datos en archivo JSON
        file_put_contents($dataFile, json_encode($data));
        echo json_encode(['success' => true, 'message' => 'Datos recibidos correctamente']);
    } else {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Datos inválidos']);
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Servir los datos más recientes
    if (file_exists($dataFile)) {
        $data = file_get_contents($dataFile);
        echo $data;
    } else {
        echo json_encode([
            'voltaje_1' => 0,
            'voltaje_2' => 0,
            'voltaje_3' => 0,
            'corriente_1' => 0,
            'corriente_2' => 0,
            'corriente_3' => 0,
            'potencia_1' => 0,
            'potencia_2' => 0,
            'potencia_3' => 0,
            'timestamp' => date('Y-m-d H:i:s')
        ]);
    }
}
?>
