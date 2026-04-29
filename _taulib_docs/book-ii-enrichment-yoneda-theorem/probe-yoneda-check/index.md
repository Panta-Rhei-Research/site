---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_yoneda_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/probe-yoneda-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::probe_yoneda_check",
  "declaration_slug": "probe-yoneda-check",
  "kind": "def",
  "name": "probe_yoneda_check",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 65,
  "source_line_end": 90,
  "registry_ids": [
    "II.L11"
  ],
  "related_registry_items": [
    {
      "id": "II.L11",
      "title": "Probe Naturality iff Yoneda",
      "url": "/registry/object/II.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L65-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L65-L90",
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L65-L90)
- Source range: L65-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L11` — Probe Naturality iff Yoneda

## Immediate Comment / Docstring

```lean
/-- [II.L11] Probe naturality iff Yoneda check:
    verify that for tower-coherent test functions, probe naturality
    holds at every point and stage iff Yoneda representability holds. -/
```

## Source Excerpt

```lean
def probe_yoneda_check (bound db : TauIdx) : Bool :=
  go_fn [fun n => reduce n, fun n => reduce (n * n), fun n => reduce (2 * n),
         fun _ => (0 : TauIdx → TauIdx)] 0 bound db ((bound + 1) * (db + 1) * 5)
where
  go_fn (fns : List (TauIdx → TauIdx → TauIdx))
        (x : Nat) (bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else match fns with
    | [] => true
    | fn :: rest =>
      let ok := go_xk fn x 1 bound db (fuel - 1)
      ok && go_fn rest x bound db (fuel - 1)
  termination_by fuel
  go_xk (fn : TauIdx → TauIdx → TauIdx)
         (x k : Nat) (bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go_xk fn (x + 1) 1 bound db (fuel - 1)
    else
      -- fn(n, k) = fn n k: the test function at stage k
      let f_at_k := fun n => fn n k
      let probe_ok := is_probe_natural f_at_k x k
      let yoneda_ok := is_yoneda_representable f_at_k x k
      -- They should agree: both true for tower-coherent functions
      (probe_ok == yoneda_ok) && go_xk fn x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
