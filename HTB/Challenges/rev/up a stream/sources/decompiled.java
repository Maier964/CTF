import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Challenge {
  public static void main(String[] paramArrayOfString) {
    String str = "FLAG";
    Objects.requireNonNull(System.out);
    dunkTheFlag(str).stream().forEach(System.out::println);
  }
  
  private static List<String> dunkTheFlag(String paramString) {
    return Arrays.asList(
        new String[] {
             ((String)((List)((String)((List)((String)(
                (List)paramString
             .chars()   // Go trough each character (as an int)
             .mapToObj(paramInt -> Character.valueOf((char)paramInt)) // Convert each int char to a Character Object  
             .collect(Collectors.toList())  // Get the list of Character Objects
                                                      )
                .stream() // Initiate a new stream on the character object list 
                .peek(paramCharacter -> hydrate(paramCharacter)) // each char will become an Integer object with the value of the initial char + 1
                .map(paramCharacter -> paramCharacter.toString()) // convert each integer to a string now
                .reduce("", (paramString1, paramString2) -> paramString2 + paramString2) // concatenate output
                                            ) // Interpret all this as a List 
                .chars() // start converting to a stream of int chars again
                    .mapToObj(paramInt -> Character.valueOf((char)paramInt)) // Character Objects again
                    .collect(Collectors.toList()) // Create a list out of the objects
                                       ) // Interpret this as a String
                        .stream() // Starting again
                        .map(paramCharacter -> paramCharacter.toString()) // Each Character will become a String
                        .reduce(String::concat).get() // Get the String back.. wtf, this basically did nothing haha
                              ) // As a list
                            .chars() // List of ints
                            .mapToObj(paramInt -> Integer.valueOf(paramInt)) // List of Integer objects 
                            .collect(Collectors.toList()) // Get em back
                        ) // Use stream on a String now
                                .stream() // Now we're talking 
                                .map(paramInteger -> moisten(paramInteger.intValue())) // 
                                .map(paramInteger -> Integer.valueOf(paramInteger.intValue()))  
                                .map(Challenge::drench)
                                .peek(Challenge::waterlog)
                                .map(Challenge::dilute)
                                .map(Integer::toHexString)
                                .reduce("", (paramString1, paramString2) -> paramString1 + paramString1 + "O")
                )
                                    .repeat(5)  // Repeat all this from the beginning 5 times.. No way to do this with bare hands, we need a script for this
                                    
                        });
  }
  
  private static Integer hydrate(Character paramCharacter) {
    return Integer.valueOf(paramCharacter.charValue() - 1);
  }
  
  private static Integer moisten(int paramInt) {
    return Integer.valueOf((int)((paramInt % 2 == 0) ? paramInt : Math.pow(paramInt, 2.0D)));
  }
  
  private static Integer drench(Integer paramInteger) {
    return Integer.valueOf(paramInteger.intValue() << 1);
  }
  
  private static Integer dilute(Integer paramInteger) {
    return Integer.valueOf(paramInteger.intValue() / 2 + paramInteger.intValue());
  }
  
  private static byte waterlog(Integer paramInteger) {
    paramInteger = Integer.valueOf((((paramInteger.intValue() + 2) * 4 % 87 ^ 0x3) == 17362) ? (paramInteger.intValue() * 2) : (paramInteger.intValue() / 2));
    return paramInteger.byteValue();
  }

}
