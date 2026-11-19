var uri = window.location.protocol + '//' + window.location.host
			var api = [
				{
					'name': '/info',
					'example': '/info',
					'description': 'This method return current info about MinersWorldCoin network.',
					'method': 'GET',
					'id': 'info'
				}, {
					'name': '/price',
					'example': '/price',
					'description': 'This method return info about price.',
					'method': 'GET',
					'id': 'price-info'
				}, {
					'name': '/height/int:height',
					'example': '/height/1',
					'description': 'This method return block info by given height.',
					'base': '/height/',
					'method': 'GET',
					'id': 'height',
					'params': [
						{
							'title': 'height',
							'description': 'Block height',
							'example': 1,
							'key': true
						}, {
							'title': 'offset',
							'description': 'Offset of transactions list',
							'default': 0
						}
					]
				}, {
					'name': '/block/string:hash',
					'example': '/block/f0f04d06d8676e4644e2dd1820e8e49fd8a970a03fa31abe35f1bb629f4c00b4',
					'description': 'This method return block info by given hash.',
					'base': '/block/',
					'method': 'GET',
					'id': 'block',
					'params': [
						{
							'title': 'hash',
							'description': 'Block hash',
							'example': 'f0f04d06d8676e4644e2dd1820e8e49fd8a970a03fa31abe35f1bb629f4c00b4',
							'key': true
						}, {
							'title': 'offset',
							'description': 'Offset of transactions list',
							'default': 0
						}
					]
				}, {
					'name': '/header/string:hash',
					'example': '/header/f0f04d06d8676e4644e2dd1820e8e49fd8a970a03fa31abe35f1bb629f4c00b4',
					'description': 'This method return block header by given hash.',
					'base': '/header/',
					'method': 'GET',
					'id': 'header',
					'params': [
						{
							'title': 'hash',
							'description': 'Header hash',
							'example': 'f0f04d06d8676e4644e2dd1820e8e49fd8a970a03fa31abe35f1bb629f4c00b4',
							'key': true
						}
					]
				}, {
					'name': '/range/int:height',
					'example': '/range/100?offset=3',
					'description': 'This method return range of blocks staring from certain height.',
					'base': '/range/',
					'method': 'GET',
					'id': 'range',
					'params': [
						{
							'title': 'height',
							'description': 'Height of range start',
							'example': 1,
							'key': true
						}, {
							'title': 'offset',
							'description': 'Number of blocks required',
							'example': 3,
							'default': 30
						}
					]
				}, {
					'name': '/balance/string:address',
					'example': '/balance/98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
					'description': 'This method return address balance.',
					'base': '/balance/',
					'method': 'GET',
					'id': 'balance',
					'params': [
						{
							'title': 'address',
							'description': 'Request address',
							'example': '98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59 ',
							'key': true
						}
					]
				}, {
					'name': '/mempool/string:address',
					'example': '/mempool/98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
					'description': 'This method return address mempool transactions.',
					'base': '/mempool/',
					'method': 'GET',
					'id': 'mempool',
					'params': [
						{
							'title': 'address',
							'description': 'Request address',
							'example': '98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
							'key': true
						}
					]
				}, {
					'name': '/unspent/string:address',
					'example': '/unspent/98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59?amount=1',
					'description': 'This method return address unspent outputs.',
					'base': '/unspent/',
					'method': 'GET',
					'id': 'unspent',
					'params': [
						{
							'title': 'address',
							'description': 'Request address',
							'example': '98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
							'key': true
						}, {
							'title': 'amount',
							'description': 'Required amount',
							'example': 1,
							'default': 0
						}
					]
				}, {
					'name': '/history/string:address',
					'example': '/history/98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
					'description': 'This method return list of address transaction hashes.',
					'base': '/history/',
					'method': 'GET',
					'id': 'history',
					'params': [
						{
							'title': 'address',
							'description': 'Request address',
							'example': '98AUvgXPjAdKHj3FqwAPJNpd8XergXBL59',
							'key': true
						}, {
							'title': 'offset',
							'description': 'Offset of transactions list',
							'example': 0,
							'default': 0
						}
					]
				}, {
					'name': '/transaction/string:hash',
					'example': '/transaction/1a69b5427a536a5b72678b1d10c1372a807937acc8677cf0f804d430f9dc7133',
					'description': 'This method return info about transaction.',
					'base': '/transaction/',
					'method': 'GET',
					'id': 'transaction',
					'params': [
						{
							'title': 'hash',
							'description': 'Transaction hash',
							'example': '1a69b5427a536a5b72678b1d10c1372a807937acc8677cf0f804d430f9dc7133',
							'key': true
						}
					]
				}, {
					'name': '/hash/int:height',
					'example': '/hash/1',
					'description': 'Return the block hash at a given height.',
					'base': '/hash/',
					'method': 'GET',
					'id': 'hash-by-height',
					'params': [{
						'title': 'height',
						'description': 'Block height',
						'example': 1,
						'key': true
					}]
				}, {
					'name': '/mempool',
					'example': '/mempool',
					'description': 'This method return info about mempool.',
					'method': 'GET',
					'id': 'mempool-info'
				}, {
					'name': '/peers',
					'example': '/peers',
					'description': 'This method return info about peers.',
					'method': 'GET',
					'id': 'peers-info'
				}, {
					'name': '/supply',
					'example': '/supply',
					'description': 'This method return info about current coins supply.',
					'method': 'GET',
					'id': 'supply'
				}, {
					'name': '/supply/plain',
					'example': '/supply/plain',
					'description': 'Return circulating supply as a whole-MWC plain-text value.',
					'method': 'GET',
					'id': 'supply-plain'
				}, {
					'name': '/stats',
					'example': '/stats',
					'description': 'Return API uptime, request counts, and active subscription counts.',
					'method': 'GET',
					'id': 'api-stats'
				}, {
					'name': '/fee',
					'example': '/fee',
					'description': 'This method return recomended transaction fee.',
					'method': 'GET',
					'id': 'fee'
				}, {
					'name': '/fee-estimates',
					'example': '/fee-estimates',
					'description': 'Return live node fee estimates by confirmation target in sat/vB.',
					'method': 'GET',
					'id': 'fee-estimates'
				}, {
					'name': '/decode/string:raw',
					'example': '/decode/010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff200162042e1b57690877ffff7c000000000f2f2f6e6f64655374726174756d2f2f00000000040000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9005ed0b2000000001976a914304e4c83aa793b3ca04ea0d979b2e68ab15f7b6b88ac008c8647000000001976a914419588e5f5831c95fab98e30cf80755f5a324d3588ac0064fc4e050000001976a91483f381d735e04c09d0a60130f6caa0f80ae6824b88ac0120000000000000000000000000000000000000000000000000000000000000000000000000',
					'description': 'This method return decoded info about transaction.',
					'base': '/decode/',
					'method': 'GET',
					'id': 'decode',
					'params': [
						{
							'title': 'transaction',
							'description': 'Signed transaction',
							'example': '010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff200162042e1b57690877ffff7c000000000f2f2f6e6f64655374726174756d2f2f00000000040000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9005ed0b2000000001976a914304e4c83aa793b3ca04ea0d979b2e68ab15f7b6b88ac008c8647000000001976a914419588e5f5831c95fab98e30cf80755f5a324d3588ac0064fc4e050000001976a91483f381d735e04c09d0a60130f6caa0f80ae6824b88ac0120000000000000000000000000000000000000000000000000000000000000000000000000',
							'key': true
						}
					]
				}, {
					'name': '/broadcast',
					'example': '/broadcast',
					'description': 'This method broadcast raw signed transaction to MinersWorldCoin network.',
					'method': 'POST',
					'id': 'broadcast',
					'response': {
						'result': '8d0f52a1177c7a954cf4f952532c49c8d55f9437539b544d92f83c14e1929950',
						'error': null,
						'id': 'api-server'
					},
					'params': [
						{
							'title': 'raw',
							'description': 'Signed raw transaction'
						}
					]
				}
			]

			for (var i = 0; i < api.length; i++) {
				var options = ''
				if (api[i].params != undefined) {
					var params = api[i].params
					for (var j = 0; j < params.length; j++) {
						options += `
							<div class="example-input input-group mt-3">
								<div class="input-group-prepend">
									<span class="input-group-text">
										${params[j].title}
									</span>
								</div>
								<input type="text" data-example="${params[j].example != undefined ? params[j].example : ''}" data-name="${params[j].title}" data-key="${params[j].key != undefined ? params[j].key : 'false'}" class="form-control docs-input" placeholder="${params[j].description} ${params[j].default != undefined ? `(default: ${params[j].default})` : ''}">
							</div>`
					}
				}

				var content = `
					<div class="card mb-3 api-doc-block" data-example-base="${uri}${api[i].base}" data-request-method="${api[i].method}">
						<div class="card-header">
							<span>
								<span class="mr-1 badge badge-success">${api[i].method}</span>
							</span>
							<b>${api[i].name}</b>
							<div class="float-right">
								<button style="padding: 0rem .5rem;" class="btn btn-primary btn-sm" onclick="docs('${api[i].id}', '${api[i].method}')">
									Run <span class="entypo right"></span>
								</button>
							</div>
						</div>
						<div class="card-body">
							<div class="row">
								<div class="col-12">
									<div class="mb-3">
										${api[i].description}
									</div>
									<div id="${api[i].id}">
										<div class="card">
											<div class="card-header" style="padding: .5rem 1.25rem;">
												<a id="${api[i].id}-link" href="${uri}${api[i].example}" class="doc-link" target="_blank">
													${uri}${api[i].example}
												</a>
											</div>
											<pre class="json-display d-none"></pre>
											<span class="loading">
												<div class="text-center">
													<div class="spinner-border" role="status" style="margin: 20px;">
														<span class="sr-only">Loading...</span>
													</div>
												</div>
											</span>
										</div>
										${options}
									</div>
								</div>
							</div>
						</div>
					</div>`

				$('#docs').append(content)
				if (api[i].response == undefined) {
					docs(api[i].id)
				} else {
					display(api[i].id, api[i].response)
				}
			}

			function request(url, method, data) {
				return Promise.resolve($.ajax({
					'method': method,
					'url': url,
					'data': data
				})).then(function(data) {
					return data
				})
			}

			function docs(tag, method = 'GET') {
				$(`#${tag} pre`).addClass('d-none')
				$(`#${tag} span.loading`).removeClass('d-none')

				var link = $(`#${tag}-link`).attr('href')
				var params = {}

				if (method == 'POST') { params = inputs($(`#${tag}`))[1] }

				request(link, method, params).then(function(data) {
					display(tag, data)
				})
			}

			function display(tag, data) {
				if (tag === 'supply-plain') {
					var wholeMwc = Number(String(data).trim())
					var display = Number.isFinite(wholeMwc)
						? `${wholeMwc.toLocaleString('en-GB')} MWC`
						: String(data)
					$(`#${tag} pre`).text(display).addClass('json-editor-blackbord').removeClass('d-none')
					$(`#${tag} span.loading`).addClass('d-none')
					return
				}
				new JsonEditor(`#${tag} pre`, data)
				$(`#${tag} .json-literal-number`).each(function() {
					var number = $(this)
					var raw = number.text()
					var key = number.closest('li').children('.json-property').text().replace(/\"/g, '')
					if (key === 'supply' && /^\d+$/.test(raw)) {
						var mwc = Number(raw) / 100000000
						number.after(`<span class="supply-readable"> (${mwc.toLocaleString('en-GB', { maximumFractionDigits: 8 })} MWC)</span>`)
					}
				})
				$(`#${tag} pre`).removeClass('d-none')
				$(`#${tag} span.loading`).addClass('d-none')
			}

			function inputs(docs) {
				var params = {}
				var base = docs.attr('data-example-base')

				docs.find('.example-input').each(function() {
					var input = $(this).find('input')
					var name = input.attr('data-name')
					var example = input.attr('data-example')
					var key = JSON.parse(input.attr('data-key'))

					var data = input.val() != '' ? input.val() : example

					if (key) {
						base += data
					} else {
						if (data != '') { params[name] = data }
					}
				})

				return [base, params]
			}

			$('.docs-input').on('keyup', function() {
				var docs = $(this).closest('.api-doc-block')
				var method = docs.attr('data-request-method')

				if (method == 'GET') {
					var link = docs.find('.doc-link')

					var data = inputs(docs)
					var base = data[0]
					var params = data[1]

					if (Object.keys(params).length > 0) { base += '?' }
					base += $.param(params)
					link.attr('href', base)
					link.text(base)
				}
			})
