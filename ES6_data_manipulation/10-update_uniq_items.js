export default function updateUniqueItems(groceriesList) {
  if (!(groceriesList instanceof Map)) {
    throw new Error('Cannot process');
  }

  groceriesList.forEach((quantity, item) => {
    if (quantity === 1) {
      groceriesList.set(item, 100);
    }
  });
}
