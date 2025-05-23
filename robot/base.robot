*** Settings ***
Documentation     Arquivo para testar requisições em uma API REST
Library           RequestsLibrary
Library           Collections
Library    BuiltIn
Library    JsonLibrary

*** Variables ***
${BASE_URL}         https://reqres.in
${API_KEY}          reqres-free-v1
${email}            eve.holt@reqres.in
${senha}            pistol
${id}               04
${email_atualizado}    iza.holt@reqres.in  
${senha_atualizada}    123456pistol

*** Test Cases ***
Cenário: POST Cadastrar usuário 200
    [Tags]    POST
    Criar Sessao
    POST Endpoint /register
    Validar Status Code   200
    Validar Se Contém Chave    token

Cenário: GET Todos os usuários 200
    [Tags]    GET
    Criar Sessao
    GET Endpoint api/users
    Validar todos os usuarios na response
    Validar Status Code    200

Cenário: PUT Atualizar usuário 200
    [Tags]    PUT
    Criar Sessao
    PUT Endpoint /users/${id}
    Validar Status Code   200

Cenário: DELETE Deletar usuário
    [Tags]    DELETE
    Criar Sessao
    DELETE Endpoint /users/${id}
    Validar Status Code    204

*** Keywords ***
Criar Sessao
    Create Session    APIReqRes    ${BASE_URL}

POST Endpoint /register
    &{payload}=    Create Dictionary    email=${email}    password=${senha}
    ${headers}=    Create Dictionary    Content-Type=application/json    x-api-key=${API_KEY}
    ${response}=   POST On Session    APIReqRes    /api/register    headers=${headers}    json=${payload}

    Log To Console    Response: ${response.json()}
    Log    ${response.status_code}
    Log    ${response.json()}

    Set Global Variable    ${response}

Validar Status Code
    [Arguments]    ${esperado}
    Should Be Equal As Integers    ${response.status_code}    ${esperado}

Validar Se Contém Chave
    [Arguments]    ${chave}
    Dictionary Should Contain Key    ${response.json()}    ${chave}

GET Endpoint api/users
    ${headers}=    Create Dictionary    x-api-key=${API_KEY}
    ${response}=   GET On Session    APIReqRes    api/users    headers=${headers}
    Set Global Variable    ${response}


Validar todos os usuarios na response
    ${json}=    Convert To Dictionary    ${response.json()}
    Log    ${json}
    Dictionary Should Contain Key    ${json}    data
    ${length}=    Get Length    ${json["data"]}
    Should Be True    ${length} > 0
        
PUT Endpoint /users/${id}
    &{payload}=    Create Dictionary    email=${email}    password=${senha_atualizada}
    ${headers}=    Create Dictionary    Content-Type=application/json    x-api-key=${API_KEY}
    ${response}=   PUT On Session    APIReqRes    /api/users/${id}    headers=${headers}    json=${payload}

    Log To Console    Response: ${response.json()}
    Log    ${response.status_code}
    Log    ${response.json()}

    Set Global Variable    ${response}

DELETE Endpoint /users/${id}
    ${headers}=    Create Dictionary    Content-Type=application/json    x-api-key=${API_KEY}
    ${response}=   DELETE On Session    APIReqRes    /api/users/${id}    headers=${headers}

    Log To Console    Response Code: ${response.status_code}
    Set Global Variable    ${response}

    

# Este projeto foi ajustado com orientação do ChatGPT,
# que sugeriu incluir os cabeçalhos' em todas as requisições HTTP.
