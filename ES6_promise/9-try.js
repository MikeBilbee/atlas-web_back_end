export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const quotient = mathFunction();
    queue.push(quotient);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
