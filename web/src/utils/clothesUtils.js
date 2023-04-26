export const formatClothesFileName = (rootName, category, objID) => {
  const objIDLength = objID.toString().length;
  if (objIDLength >= 3) {
    return rootName + "^" + category.toLowerCase() + "_" + objID + "_u.ydd";
  } else if (objIDLength === 2) {
    return rootName + "^" + category.toLowerCase() + "_0" + objID + "_u.ydd";
  } else if (objIDLength === 1) {
    return rootName + "^" + category.toLowerCase() + "_00" + objID + "_u.ydd";
  }
};
