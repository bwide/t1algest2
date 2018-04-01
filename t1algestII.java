import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.stream.Stream;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.IntStream;

class T1 {
    public static void main(String[] args) {
        String path = args[0];
        File file = new File(path);

        Map<String, Set<Integer[]>> colorsDict = new HashMap<String, Set<Integer[]>>();

        try(BufferedReader br = new BufferedReader(new FileReader(file))) {
            br.readLine();
            for(String line; (line = br.readLine()) != null; ) {
                String[] lineContents = line.split(" ");
                String color = lineContents[4];
                lineContents = Arrays.copyOf(lineContents, 4);
                int[] coordinates = Arrays.stream(lineContents).mapToInt(Integer::parseInt).toArray();
                
                IntStream streamX = IntStream.rangeClosed(coordinates[0], coordinates[2]-1);
                Integer[] rangeX = streamX.boxed().toArray(Integer[]::new);

                IntStream streamY = IntStream.rangeClosed(coordinates[1], coordinates[3]-1);
                Integer[] rangeY = streamY.boxed().toArray(Integer[]::new);

                System.out.println("started cartesian product");
                Set<Integer[]> squares = cartesianProduct(rangeX, rangeY);
                System.out.println("done cartesian product");

                for( String key : colorsDict.keySet() ){
                    if(key!=color){
                        Set<Integer[]> newCoordinates = colorsDict.get(key);
                        newCoordinates.removeAll(squares);
                        colorsDict.put(key, newCoordinates);
                    }
                }

                if (colorsDict.containsKey(color))
                    colorsDict.get(color).addAll(squares);
                else
                    colorsDict.put(color, squares);

            }
        } catch(Exception e) {
            System.out.println(e);
        }

        // for (String key : colorsDict.keySet()){
        //     System.out.print( key + ": ");
        //     for(Integer[] tuple : colorsDict.get(key)){
        //         System.out.print( Arrays.toString(tuple) );
        //     }
        //     System.out.println();
        // }

        for (String key : colorsDict.keySet()){
            System.out.println( key + ": " + colorsDict.get(key).size());
        }
    }

    public static Set<Integer[]> cartesianProduct(Integer[] s1, Integer[] s2) {
        int size1 = s1.length;
        int size2 = s2.length;
        Set<Integer[]> result = new HashSet<Integer[]>(); //new int[size1 * size2][2];
        for (int i = 0, d = 0; i < size1; ++i) {
            for (int j = 0; j < size2; ++j, ++d) {
                Integer[] tuple = { s1[i], s2[j] };
                result.add( tuple );
            }
        }
        return result;
    }
}