function myFucntion(number) {
  if (number > 10) return;

  console.log(number);
  myFucntion(number + 1);
}

myFucntion(1);
