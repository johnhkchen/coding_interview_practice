main = do 
  -- This is Haskell!
  putStrLn "Hello World! Who is this?"
  name <- getLine
  putStrLn ("Pleased to meet you, "++name++"!")