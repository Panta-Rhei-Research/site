---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_cofinal_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/primorial-cofinal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::primorial_cofinal_check",
  "declaration_slug": "primorial-cofinal-check",
  "kind": "def",
  "name": "primorial_cofinal_check",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 102,
  "source_line_end": 111,
  "registry_ids": [
    "III.T09"
  ],
  "related_registry_items": [
    {
      "id": "III.T09",
      "title": "Primorial Cofinality",
      "url": "/registry/object/III.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L102-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.PrimorialLadder",
        "url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L102-L111",
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

- Module: [TauLib.BookIII.Spectral.PrimorialLadder](/verify/taulib/docs/book-iii-spectral-primorial-ladder/)
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L102-L111)
- Source range: L102-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T09` — Primorial Cofinality

## Immediate Comment / Docstring

```lean
/-- [III.T09] Primorial cofinality: for each N ≤ bound, there exists k
    such that Prim(k) ≥ N. Checking at primorial levels is sufficient. -/
```

## Source Excerpt

```lean
def primorial_cofinal_check (bound : TauIdx) : Bool :=
  go 1 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      let k := cofinal_level n
      primorial k >= n && go (n + 1) (fuel - 1)
  termination_by fuel
```
