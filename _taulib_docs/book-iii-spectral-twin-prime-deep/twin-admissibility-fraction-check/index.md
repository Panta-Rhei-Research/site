---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_admissibility_fraction_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::twin_admissibility_fraction_check",
  "declaration_slug": "twin-admissibility-fraction-check",
  "kind": "def",
  "name": "twin_admissibility_fraction_check",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 184,
  "source_line_end": 196,
  "registry_ids": [
    "III.P45"
  ],
  "related_registry_items": [
    {
      "id": "III.P45",
      "title": "Twin Admissibility Fraction",
      "url": "/registry/object/III.P45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L184-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L184-L196",
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/verify/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L184-L196)
- Source range: L184-L196
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P45` — Twin Admissibility Fraction

## Immediate Comment / Docstring

```lean
/-- [III.P45] At each odd prime p ≥ 3, exactly (p-2) out of p residue classes
    are twin-admissible. For p=2, exactly 0 out of 2 (since both r=0 and
    r=1 fail: r=0 has r%2=0, r=1 has (r+2)%2=1%2≠0 but r=1 has r%2=1≠0
    and 3%2=1≠0... actually for p=2: r=1 gives r%2=1, (r+2)%2=1, so admissible.
    r=0 gives r%2=0, blocked. So p=2 has 1 admissible. We check p ≥ 3 gives p-2. -/
```

## Source Excerpt

```lean
def twin_admissibility_fraction_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > db then true
    else
      let p := nth_prime i
      if p < 3 then go (i + 1) (fuel - 1)
      else
        let admissible := count_admissible_at_prime p
        (admissible == p - 2) && go (i + 1) (fuel - 1)
  termination_by fuel
```
