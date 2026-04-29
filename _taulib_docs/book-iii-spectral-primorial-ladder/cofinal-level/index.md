---
{
  "projection_kind": "taulib_declaration",
  "title": "cofinal_level",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/cofinal-level/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::cofinal_level",
  "declaration_slug": "cofinal-level",
  "kind": "def",
  "name": "cofinal_level",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 91,
  "source_line_end": 98,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L91-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L91-L98",
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
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L91-L98)
- Source range: L91-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T09` — Primorial Cofinality

## Immediate Comment / Docstring

```lean
/-- [III.T09] Find the smallest primorial level k such that Prim(k) ≥ n. -/
```

## Source Excerpt

```lean
def cofinal_level (n : TauIdx) : TauIdx :=
  go 0 (n + 1)
where
  go (k fuel : Nat) : TauIdx :=
    if fuel = 0 then k
    else if primorial k >= n then k
    else go (k + 1) (fuel - 1)
  termination_by fuel
```
