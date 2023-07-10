import React from 'react';

export const Handbook_report1= () => {
  return (
    <div className="container">
      <h1>2</h1>
      <div>
        <form action="" method="post">
          <div>
            <label htmlFor="dateTo">До даты:</label>
            <input type="date" id="dateTo" name="dateTo" />
          </div>
          <div>
            <label htmlFor="dateAfter">После :</label>
            <input type="date" id="dateAfter" name="dateAfter" />
          </div>
          <div className="form-check">
            <input className="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" />
            <label className="form-check-label" htmlFor="flexRadioDefault1">
              1
            </label>
          </div>
          <div className="form-check">
            <input className="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked />
            <label className="form-check-label" htmlFor="flexRadioDefault2">
              1
            </label>
          </div>
          <div>
          <h5>Маштабирование </h5>
          <select className="form-select" aria-label="Default select example">
            <option selected>Open this select menu</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>
          </div>
          <div>
          <h5>Счет </h5>
          <select className="form-select" aria-label="Default select example">
            <option selected>Open this select menu</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>
          </div>
          <div className="card-columns col-sm-12">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Ведомственная классификация</h5>
                <div className="row align-items-end">
                  <div className="col-sm-6 field-edit">
                    <div id="ControlHost_ParticipantTab-Paper-Elections-Document-Status_iAuthStatus1" className="viAuthStatus1">
                      <div className="form-group">
                        <div className="validator-container">
                          <div className="dropdown bootstrap-select show-tick form-control iAuthStatus1">
                            <select
                              name="ControlHost:ParticipantTab-Paper-Elections-Document-Status:iAuthStatus1:iAuthStatus1"
                              id="ControlHost_ParticipantTab-Paper-Elections-Document-Status_iAuthStatus1_iAuthStatus1"
                              className="form-control selectpicker show-tick iAuthStatus1"
                              data-size="15"
                              data-live-search="true"
                              tabIndex={-98}
                            >
                              <option value=""></option>
                              <option value="Pend">1</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="px-2 align-items-end">
            <a className="btn btn-primary SaveEdits mr-1" href="javascript:alert('hi');">Сохранить</a>
          </div>
          <div className="card-columns col-sm-12">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Функциональная классификация</h5>
                <div className="row align-items-end">
                  <div className="col-sm-6 field-edit">
                    <div id="ControlHost_ParticipantTab-Paper-Elections-Document-Status_iAuthStatus1" className="viAuthStatus1">
                      <div className="form-group">
                        <div className="validator-container">
                          <div className="dropdown bootstrap-select show-tick form-control iAuthStatus1">
                            <select
                              name="ControlHost:ParticipantTab-Paper-Elections-Document-Status:iAuthStatus1:iAuthStatus1"
                              id="ControlHost_ParticipantTab-Paper-Elections-Document-Status_iAuthStatus1_iAuthStatus1"
                              className="form-control selectpicker show-tick iAuthStatus1"
                              data-size="15"
                              data-live-search="true"
                              tabIndex={-98}
                            >
                              <option value=""></option>
                              <option value="Pend">1</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="px-2 align-items-end">
            <a className="btn btn-primary SaveEdits mr-1" href="javascript:alert('hi');">Сохранить</a>
          </div>
          <div className="restart">
          <button type="button" className="btn btn-primary btn-lg">Сгенерировать</button>
          <button type="button" className="btn btn-secondary btn-lg">Отмена</button>
          </div>
        </form>
      </div>
    </div>
  );
};



export default Handbook_report1;