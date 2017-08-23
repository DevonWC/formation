import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Vector;
import java.util.List;

public class start {
    
        public static void main(String [] args)
        {

            List<aluno> lista = new ArrayList<>();
    
            aluno a1 = new aluno();
            a1.set("jeremias");
    
            aluno a2 = new aluno();
            a2.set("gertrudes");

            colecao.adicionar(lista, a1, a2);

            System.out.println(colecao.contar(lista));
            colecao.imprimir(lista);          
            colecao.remover(lista, a1);
            colecao.imprimir(lista);
            System.out.println(colecao.contar(lista));
                
        }
    
    }

class aluno {  

    String nome;

    //retorna o atributo nome do objeto aluno
    public String get()
    {
        return nome;
    }

    //modifica o atributo nome do objeto aluno
    public void set(String nomea)
    {
        nome = nomea;
    }
}  

class colecao {

    //adiciona objeto(s) do tipo aluno a uma lista
    public static void adicionar(List lst, aluno...args)
    {
        for (aluno arg : args) {
            lst.add(arg);
        }
    }

    //retorna todos os elementos da lista
    public static void imprimir(List list)
    {
        System.out.println(list);
    }

    //remove objetos da lista
    public static void remover(List lst, aluno...args)
    {
        for (aluno arg : args){
            lst.remove(arg);
        }
    }

    //conta objetos na lista
    public static int contar(List l){
        return l.size();
    }

}
