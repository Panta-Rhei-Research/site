---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_growth_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/primorial-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::primorial_growth_check",
  "declaration_slug": "primorial-growth-check",
  "kind": "def",
  "name": "primorial_growth_check",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 76,
  "source_line_end": 84,
  "registry_ids": [
    "III.D19"
  ],
  "related_registry_items": [
    {
      "id": "III.D19",
      "title": "Primorial Ladder",
      "url": "/registry/object/III.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L76-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L76-L84",
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
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L76-L84)
- Source range: L76-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D19` — Primorial Ladder

## Immediate Comment / Docstring

```lean
/-- [III.D19] Primorial growth: Prim(k+1) > Prim(k) (strictly increasing). -/
```

## Source Excerpt

```lean
def primorial_growth_check (bound : TauIdx) : Bool :=
  go 1 (bound + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > bound then true
    else
      primorial (k + 1) > primorial k && go (k + 1) (fuel - 1)
  termination_by fuel
```
