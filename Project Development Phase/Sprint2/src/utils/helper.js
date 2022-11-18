export const emailRegex = /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/;

let api_keys = [];
api_keys[0] = {
  id: import.meta.env.VITE_ADZUNA_API_ID_1,
  key: import.meta.env.VITE_ADZUNA_API_KEY_1,
};
api_keys[1] = {
  id: import.meta.env.VITE_ADZUNA_API_ID_2,
  key: import.meta.env.VITE_ADZUNA_API_KEY_2,
};
api_keys[2] = {
  id: import.meta.env.VITE_ADZUNA_API_ID_3,
  key: import.meta.env.VITE_ADZUNA_API_KEY_3,
};

export const urlRegex =
  /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+(:[0-9]+)?|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/;

export const BASE_URL = import.meta.env.VITE_BACKEND_ENDPOINT;

const getRandomNumber = () => {
  const randomnumber = Math.floor(Math.random() * 3);
  return randomnumber;
};

export const getBaseUrl = (query) => {
  const rand = getRandomNumber();
  return `http://api.adzuna.com/v1/api/jobs/in/search/1?app_id=${api_keys[rand].id}&app_key=${api_keys[rand].key}&results_per_page=15&what=${query}&content-type=application/json`;
};

export const getBaseUrl_with_skills = (query, skills) => {
  const rand = getRandomNumber();
  return `http://api.adzuna.com/v1/api/jobs/in/search/1?app_id=${
    api_keys[rand].id
  }&app_key=${
    api_keys[rand].key
  }&results_per_page=15&what=${query}&what_and=${skills.join(
    " "
  )}&&content-type=application/json`;
};
