export function convertArrayToArrayDict(array, dict, valueKey, arrayKeysText, separator) {
  const l = [];
  // console.log(JSON.stringify(array));
  // console.log(JSON.stringify(dict));
  // console.log(JSON.stringify(valueKey));
  for (let i = 0; i < array.length; i += 1) {
    let obj = null;
    if (dict) {
      obj = dict[array[i]];
    } else {
      obj = array[i];
    }
    // console.log(`obj ${obj}`);
    let textString = '';
    for (let j = 0; j < arrayKeysText.length; j += 1) {
      if (j !== 0) {
        textString += `${separator}`;
      }
      textString += `${obj[arrayKeysText[j]]}`;
    }
    l.push({ value: valueKey ? obj[valueKey] : obj, text: textString });
  }
  // console.log('====');
  // console.log(l);
  // console.log('====');
  return l;
}

export function convertDictToArray(selectList, valueKey) {
  const l = [];
  for (let i = 0; i < selectList.length; i += 1) {
    const obj = selectList[i];
    l.push(obj[valueKey]);
  }
  return l;
}
