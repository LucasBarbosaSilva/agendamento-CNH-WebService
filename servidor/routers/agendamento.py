from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import List

router = APIRouter(prefix="/agendamento")

listaHorarios = [
    {
        'id': 1,
        'data': '01/02/2024',
        'hora': '08:00',
        'agendado': True
    },
    {
        'id': 2,
        'data': '01/02/2024',
        'hora': '08:30',
        'agendado': False
    },
    {
        'id': 3,
        'data': '01/02/2024',
        'hora': '09:00',
        'agendado': False
    },
    {
        'id': 4,
        'data': '02/02/2024',
        'hora': '08:00',
        'agendado': False
    },
    {
        'id': 5,
        'data': '02/02/2024',
        'hora': '08:30',
        'agendado': True
    },
    {
        'id': 6,
        'data': '02/02/2024',
        'hora': '09:00',
        'agendado': False
    },
    {
        'id': 7,
        'data': '01/02/2024',
        'hora': '09:30',
        'agendado': False
    },
    {
        'id': 8,
        'data': '02/02/2024',
        'hora': '10:00',
        'agendado': False
    },
    {
        'id': 9,
        'data': '02/02/2024',
        'hora': '10:30',
        'agendado': False
    },
    {
        'id': 10,
        'data': '04/02/2024',
        'hora': '13:00',
        'agendado': False
    }
]

class AgendamentoResponse(BaseModel):
    id: int
    data: str
    hora: str
    agendado: bool
    
class AgendamentoRequest(BaseModel):
    data: str
    hora: str
    agendado: bool

@router.get("", response_model=List[AgendamentoResponse])
def listarAgendamentos() -> List[AgendamentoResponse]:
    return listaHorarios

@router.delete("/{id_agendamento}", status_code=204)
def deletarAgendamentos(
        id_agendamento: int,
    ):
    index = -1
    for i, x in enumerate(listaHorarios):
        if(x['id'] == id_agendamento):
            index = i
    listaHorarios.pop(index)

@router.put("/{id_agendamento}", status_code=200)
def agendar(
        id_agendamento: int,
        agendamento_request: AgendamentoRequest
    ) -> AgendamentoResponse:
    index = 0
    
    for i, x in enumerate(listaHorarios):
        if(x['id'] == id_agendamento):
            x['data'] = agendamento_request.data
            x['hora'] = agendamento_request.hora
            x['agendado'] = agendamento_request.agendado
            agendamento = x
            index = i
            break
    listaHorarios[index] = agendamento        
    return agendamento