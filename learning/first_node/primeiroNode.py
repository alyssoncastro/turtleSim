

#LINHA SHEBANG: definição de qual interpretador de script será usado
#!/usr/bin/env python3

#importando os módulos necessários para criar o nó ROS e controlar a tartaruga.
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


#Inicializando o nome do nó, criando o publisher, o time, a mensagem Twist e um contrlador.

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        print("funciona?")
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.counter = 0


#movimento hexagonal da tartaruga.
    def move_turtle(self):
        if self.counter < 5: # altere o valor aqui para o número de vezes que deseja desenhar o triângulo
            for i in range(3):
                self.twist_msg_.linear.x = 3.0 #tamanho da área que a tartaruga irá pecorrer.
                self.publisher_.publish(self.twist_msg_)
                time.sleep(1.0)
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 1.0
                self.publisher_.publish(self.twist_msg_)
                time.sleep(1.5)
                self.twist_msg_.angular.z = 0.0
            self.counter += 1
        else:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)

#função inicialização do ROS e o nó, executando o loop de eventos do ROS e deligando o nó quando o loop é interrompido
def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()
    
    
#verificação se o comando é um programa principal. 
if __name__ == '__main__':
    main()