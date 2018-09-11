HOST_WORKDIR="$$(pwd)"
HOST_PORT=5000

GUEST_WORKDIR=/usr/src/app
GUEST_PORT=5000

IMAGE=conflict_solver


cleanup:
	@-docker container stop $(IMAGE)
	@-docker image rm $(IMAGE)
	
image:
	@-make cleanup
	@docker image build -t $(IMAGE) .

database:
	@-rm '$(IMAGE).db'
	@sqlite3 '$(IMAGE).db' < conflict_solver_migrations/20180329_init.ddl && \
		sqlite3 '$(IMAGE).db' < conflict_solver_migrations/20180331_init.dml

service:
	@make database
	@echo "Working with directory $(HOST_WORKDIR)"
	@docker container run --rm -v "$(HOST_WORKDIR):$(GUEST_WORKDIR)" -p $(HOST_PORT):$(GUEST_PORT) --name $(IMAGE) $(IMAGE)
