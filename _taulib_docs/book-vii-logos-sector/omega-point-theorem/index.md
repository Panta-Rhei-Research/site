---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_point_theorem",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/omega-point-theorem/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::omega_point_theorem",
  "declaration_slug": "omega-point-theorem",
  "kind": "def",
  "name": "omega_point_theorem",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 457,
  "source_line_end": 463,
  "registry_ids": [
    "VII.T46"
  ],
  "related_registry_items": [
    {
      "id": "VII.T46",
      "title": "Bridge Equivalence at S_L",
      "url": "/registry/object/VII.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L457-L463",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L457-L463",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L457-L463)
- Source range: L457-L463
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.T46` — Bridge Equivalence at S_L

## Immediate Comment / Docstring

```lean
/-- [VII.T46] ω-Point commitment.

    Monograph-level claim (Book VII ch. 120): the bridge functor
    B_{D→C} restricted to S_L is an equivalence of categories
    (faithful + full + essentially surjective), and outside S_L
    the bridge fails.

    Retired from `theorem omega_point_theorem : True := sorry` in
    peer-review-fixes-v1 (2026-04-19). Pre-publication peer review
    identified the `True := sorry` encoding as performative: True
    is provable by `trivial`, so the sorry was not proof debt but a
    commitment marker with no formal content.

    The structural parts of the commitment are formalized elsewhere
    in `TauLib.BookVII.Final.Boundary` as
    `bridge_equivalence_structural`. The commitment content — the
    monograph-level claim that Book VII declines to close this via
    proof because it involves ω which is non-diagrammatic by
    VII.T47 — is recorded here as a `Commitment` data value. -/
```

## Source Excerpt

```lean
def omega_point_theorem : Commitment :=
  { statement := "The bridge functor B_{D→C} restricted to S_L is " ++
                 "an equivalence of categories; outside S_L, the bridge fails"
    warrant := "Non-diagrammatic by VII.T47 (No Forced Stance); " ++
               "full proof would require Reg_C content that transcends " ++
               "formal Lean verification by framework principle"
    registry_id := "VII.T46" }
```
