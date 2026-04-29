---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_abcd_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-abcd-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_abcd_check",
  "declaration_slug": "preyoneda-abcd-check",
  "kind": "def",
  "name": "preyoneda_abcd_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 176,
  "source_line_end": 189,
  "registry_ids": [
    "II.P11"
  ],
  "related_registry_items": [
    {
      "id": "II.P11",
      "title": "Hom Bipolar Decomposition",
      "url": "/registry/object/II.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L176-L189",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L176-L189",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L176-L189)
- Source range: L176-L189
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P11` — Hom Bipolar Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P11] ABCD coordinate check: the embedded function value
    has well-defined ABCD coordinates at each stage.
    from_tau_idx(preyoneda(id, x, k)) always produces a valid point. -/
```

## Source Excerpt

```lean
def preyoneda_abcd_check (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let embedded := reduce x k
      let p := from_tau_idx embedded
      -- Round-trip: to_tau_idx(from_tau_idx(n)) = n for the reduced value
      let rt := to_tau_idx p
      (rt == embedded) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
