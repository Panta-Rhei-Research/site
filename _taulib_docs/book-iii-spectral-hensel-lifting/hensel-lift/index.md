---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_lift",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-lift/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_lift",
  "declaration_slug": "hensel-lift",
  "kind": "def",
  "name": "hensel_lift",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 71,
  "source_line_end": 82,
  "registry_ids": [
    "III.T11"
  ],
  "related_registry_items": [
    {
      "id": "III.T11",
      "title": "Constructive Hensel Lifting",
      "url": "/registry/object/III.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L71-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.HenselLifting",
        "url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L71-L82",
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

- Module: [TauLib.BookIII.Spectral.HenselLifting](/verify/taulib/docs/book-iii-spectral-hensel-lifting/)
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L71-L82)
- Source range: L71-L82
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Full Hensel lift: iterate from mod p to mod p^n.
    Starts by reducing root mod p (ensures canonical starting point). -/
```

## Source Excerpt

```lean
def hensel_lift (a root p n : TauIdx) : TauIdx :=
  if p < 2 then root
  else go (root % p) p 1 n
where
  go (x pk exp fuel : Nat) : TauIdx :=
    if fuel = 0 then x
    else if exp >= n then x % (p ^ n)
    else
      let pk1 := pk * p
      let x' := hensel_step a x p pk pk1
      go x' pk1 (exp + 1) (fuel - 1)
  termination_by fuel
```
