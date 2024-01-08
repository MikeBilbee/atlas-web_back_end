export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return 0;
  }

  const filterStudents = students.filter(student => student.location === city);
  const gradeMap = new Map(newGrades.map(grade => [grade.studentId, grade.grade]));
  return filterStudents.map(student => ({
    ...student,
    grade: gradeMap.get(student.id) || "N/A"
  }));
}
