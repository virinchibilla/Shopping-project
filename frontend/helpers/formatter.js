export function boldSU(value) {
  if (['admin', 'superuser'].includes(value.toLowerCase())) {
    return `<span style="font-weight: bold">${value}</span>`;
  }
  return value;
}

export function booleanColor(value) {
  if (value.toString() === 'true') {
    return '<span style="color: green">Yes</span>';
  }
  return '<span style="color: red">No</span>';
}

export function inlineStringArray(value, separator) {
  let sep = separator;
  if (!sep) {
    sep = ', ';
  }
  if (!Array.isArray(value)) {
    return value;
  }
  let s = '';
  for (let i = 0; i < value.length; i += 1) {
    if (i !== 0) {
      s += sep;
    }
    s += value[i];
  }
  return s;
}
