---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_primorial_deep_check",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-abcdeep/radical-primorial-deep-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::radical_primorial_deep_check",
  "declaration_slug": "radical-primorial-deep-check",
  "kind": "def",
  "name": "radical_primorial_deep_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 155,
  "source_line_end": 164,
  "registry_ids": [
    "III.T78"
  ],
  "related_registry_items": [
    {
      "id": "III.T78",
      "title": "Radical Primorial 5",
      "url": "/registry/object/III.T78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L155-L164",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-abcdeep/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L155-L164",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/corpus/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L155-L164)
- Source range: L155-L164
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T78` — Radical Primorial 5

## Immediate Comment / Docstring

```lean
/-- [III.T78] Extended radical-primorial identity: rad(M_k) = M_k
    for k = 1..db. Primorials are squarefree. -/
```

## Source Excerpt

```lean
def radical_primorial_deep_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      (radical pk == pk) && (is_squarefree pk) && go (k + 1) (fuel - 1)
  termination_by fuel
```
