export default function getStudentsByLocation(studentsList, city) {
  if (!Array.isArray(studentsList)) {
    return [];
  }

  return studentsList.filter((students) => students.location === city);
}
