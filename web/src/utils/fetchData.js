export const fetchClothes = async () => {
  try {
    const response = await fetch('./clothes.json');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching clothes.json:', error);
  }
};
