import unittest
from tareas.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def test_agregar_y_listar(self):
        g = GestorTareas()
        g.agregar_tarea("Probar tarea")
        self.assertEqual(len(g.tareas), 1)
        self.assertEqual(g.tareas[0]["descripcion"], "Probar tarea")
        self.assertFalse(g.tareas[0]["completa"])

    def test_completar_tarea(self):
        g = GestorTareas()
        g.agregar_tarea("Probar tarea")
        g.completar_tarea(0)
        self.assertTrue(g.tareas[0]["completa"])

if __name__ == "__main__":
    unittest.main()
