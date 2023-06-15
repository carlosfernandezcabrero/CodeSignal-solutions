ifLowerLimitIsLessThanYear :: (Ord a, Num p) => a -> a -> p
ifLowerLimitIsLessThanYear lowerLimit year = if lowerLimit < year then 1 else 0

solution :: Integral a => a -> a
solution year = unsafePerformIO $ do
  let twoDigitsYear = year `div` 100
  let lowerLimit = twoDigitsYear * 100
  let result = twoDigitsYear + ifLowerLimitIsLessThanYear lowerLimit year

  return result