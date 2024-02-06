import api from './api';
import type { Schedule } from '@/models/schedule';

const resource = '/agendamento';

export default {
  get() {
    return api.get<Schedule[]>(`${resource}`);
  },

  update(id: number) {
    return api.put(`${resource}/${id}`);
  },
};