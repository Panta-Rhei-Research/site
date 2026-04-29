---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_primorial_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/goldbach-primorial-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::goldbach_primorial_check",
  "declaration_slug": "goldbach-primorial-check",
  "kind": "def",
  "name": "goldbach_primorial_check",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 148,
  "source_line_end": 158,
  "registry_ids": [
    "III.T64"
  ],
  "related_registry_items": [
    {
      "id": "III.T64",
      "title": "Goldbach at Primorial Levels",
      "url": "/registry/object/III.T64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L148-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L148-L158",
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/verify/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L148-L158)
- Source range: L148-L158
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T64` — Goldbach at Primorial Levels

## Immediate Comment / Docstring

```lean
/-- [III.T64] Goldbach at primorial levels: every even number up to
    min(M_k, 100) has a Goldbach representation. -/
```

## Source Excerpt

```lean
def goldbach_primorial_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let bound := min pk 100
      goldbach_check bound && go (k + 1) (fuel - 1)
  termination_by fuel
```
