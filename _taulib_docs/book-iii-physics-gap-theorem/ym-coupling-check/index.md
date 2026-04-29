---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_coupling_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/ym-coupling-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::ym_coupling_check",
  "declaration_slug": "ym-coupling-check",
  "kind": "def",
  "name": "ym_coupling_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 173,
  "source_line_end": 186,
  "registry_ids": [
    "III.D46"
  ],
  "related_registry_items": [
    {
      "id": "III.D46",
      "title": "Strong Defect Functional",
      "url": "/registry/object/III.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L173-L186",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L173-L186",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L173-L186)
- Source range: L173-L186
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D46` — Strong Defect Functional

## Immediate Comment / Docstring

```lean
/-- [III.D46] YM coupling check: the coupling is well-defined, non-zero,
    and tower-monotone (coupling changes predictably with depth). -/
```

## Source Excerpt

```lean
def ym_coupling_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let (b_ct, c_ct, _) := label_counts k
      -- Coupling well-defined: both sector products positive when both have primes
      let bp := split_zeta_b k
      let cp := split_zeta_c k
      let ok := if b_ct > 0 && c_ct > 0 then bp > 0 && cp > 0 else true
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
