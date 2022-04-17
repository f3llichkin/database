# database
Спроектировать базу данных, построить программу, обеспечивающую
взаимодействие с ней в режиме диалога для менеджера музыкальных групп.
В БД должны храниться сведения о группах: название, год образования, 
страна, состав исполнителей, положение в последнем хит-параде (может 
измениться); о репертуаре каждой группы: названия песен, композитор, автор 
текста; 
данные о последних гастролях группы: название гастрольной программы, дата 
начала и окончания гастролей, цена билета (зависит от места гастролей и 
положения в хит-параде). Возможно появление новой группы и изменения в 
составе исполнителей. Каждая песня может быть в репертуаре только одной
группы.
Менеджеру могут потребоваться следующие сведения:
 год образования, страна группы данного названия;
 репертуар наиболее популярной группы;
 автор текста, композитор и дата создания песни с данным названием;
 место и продолжительность гастролей группы данного названия;
 цена билета на концерт указанной группы;
 состав исполнителей группы данного названия, их возраст и амплуа.
Администратор может вносить следующие изменения:
 ввод новой группы;
 изменение положения группы в хит-параде;
 удаление информации об исполнителе, покинувшем группу.
3
Необходимо предусмотреть возможность выдачи:
 справки о лучших группах в хит-параде;
 отчета о гастролях групп (название, сроки, место, цена билета, репертуар с 
указанием автора)