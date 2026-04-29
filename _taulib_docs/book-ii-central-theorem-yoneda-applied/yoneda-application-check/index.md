---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_application_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/yoneda-application-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::yoneda_application_check",
  "declaration_slug": "yoneda-application-check",
  "kind": "def",
  "name": "yoneda_application_check",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 58,
  "source_line_end": 76,
  "registry_ids": [
    "II.L14"
  ],
  "related_registry_items": [
    {
      "id": "II.L14",
      "title": "Yoneda Application",
      "url": "/registry/object/II.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L58-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L58-L76",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L58-L76)
- Source range: L58-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L14` — Yoneda Application

## Immediate Comment / Docstring

```lean
/-- [II.L14] Yoneda application check: verify that the pre-Yoneda
    embedding applied to a tower-coherent function gives a tower-coherent
    result, and that Code extracts the original.

    For f = identity (tower-coherent by construction):
    1. preyoneda_embed(f, x, k) = f(reduce(x, k)) = reduce(x, k)
    2. code_extract(preyoneda(f), k, x) = preyoneda(f)(reduce(x, k))
       = f(reduce(reduce(x, k), k)) = f(reduce(x, k))
       = preyoneda(f)(x, k)

    So Code applied to the pre-Yoneda image recovers the pre-Yoneda image itself.
    This is the Yoneda lemma in action: representable presheaves are fully faithful. -/
```

## Source Excerpt

```lean
def yoneda_application_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Pre-Yoneda embedding of identity: preyoneda(id, x, k) = reduce(x, k)
      let py_val := preyoneda_embed_nat (fun n => n) x k
      -- Tower coherence: reduce(py(x, k+1), k) = py(x, k)
      let py_next := preyoneda_embed_nat (fun n => n) x (k + 1)
      let tc_ok := reduce py_next k == py_val
      -- Code extraction round-trip: code_extract(py, k, x) = py(x)
      let py_fn : TauIdx -> Int := fun n => (preyoneda_embed_nat (fun m => m) n k : Int)
      let code_val := code_extract py_fn k x
      let code_ok := code_val == (py_val : Int)
      tc_ok && code_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
