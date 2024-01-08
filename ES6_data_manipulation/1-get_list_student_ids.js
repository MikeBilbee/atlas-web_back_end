export default function getListStudents(studentsList) {
  if (!Array.isArray(studentsList)) {
    return [];
  }

  return studentsList.map((students) => students.id);
}
